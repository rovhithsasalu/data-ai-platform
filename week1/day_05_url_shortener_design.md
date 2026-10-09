# Day 05: URL Shortener System Design

## Assignment

Design a service like Bitly that accepts a long URL, creates a short URL, stores the mapping, and redirects visitors from the short URL to the original destination.

Scale assumptions from the Week 1 plan:

- 100 million new URLs per month
- 100 redirect lookups for every URL creation
- Five-year retention
- About 500 bytes per stored mapping

Approximate average traffic: 39 URL creation requests/second and 3,900 redirect requests/second. Real peak traffic may be higher; the design should state how it will scale rather than infer a fixed server count from averages.

## My first design

The submitted diagram includes:

- Users calling APIs to create or visit a URL
- A CDN/cache and load balancer
- Three application servers
- A database cluster with a writer and read replicas
- A Bitly mapping containing an ID, short URL, long URL, and user ID
- Autoscaling based on traffic
- A proposal to create a unique hash/code, store the mapping, and retry if a collision occurs
- A note distinguishing temporary (302) and permanent (301) redirects

### Gaps I identified

1. I need to make better database choices and explain constraints and trade-offs, including relational versus NoSQL storage.
2. I need to plan the backend service that creates and resolves short URLs more clearly.
3. I need to decide whether a load balancer is required and avoid guessing the number of active servers.
4. I need to define idempotency, functional and non-functional requirements, scale estimates, and latency targets.
5. I need to improve the clarity of my design diagram.

## Feedback and design refinements

### Separate the two request flows

**Create a short URL**

1. Client sends `POST /urls` with the long URL.
2. Shortener service validates the input.
3. The service generates a unique short code.
4. It stores the mapping in the primary database.
5. It returns the short URL to the client.

**Redirect a visitor**

1. Browser requests `GET /{code}`.
2. CDN or cache checks for the code. On a cache miss, the redirect service looks it up in the database.
3. Service responds with an HTTP redirect whose `Location` header contains the original URL.
4. Optional click analytics are sent asynchronously so they do not slow down the redirect path.

The CDN belongs on the redirect/read path, not in the URL-creation write path.

### Revised high-level sketch

```text
CREATE
Client -- POST /urls --> Load balancer --> Shortener service
                                            |          |
                                            |          +--> Primary database
                                            +--> Code generation

REDIRECT
Browser -- GET /{code} --> CDN/cache -- hit ----------------------+
                              | miss                              |
                              v                                   |
                         Load balancer --> Redirect service       |
                                                |                  |
                                           Cache / database        |
                                                +------------------+
Browser <-- 302 + Location: original URL -------------------------+

Optional: click event --> queue/worker --> analytics store
```

### Decisions to make and explain

- **Database:** The main lookup is `short_code -> long_url`, a key-value access pattern. A relational database is also a reasonable starting choice. Explain the requirements and trade-offs behind the choice, and what scale or query needs would lead to partitioning or another store.
- **Short-code uniqueness:** Enforce a unique constraint on the code in storage. If code generation can collide, retry after a conflict. A generated unique ID encoded as Base62 is another approach; explain its trade-offs and whether codes are guessable.
- **Idempotency:** Decide how a client retrying `POST /urls` avoids accidentally creating multiple mappings. One option is an idempotency key supplied by the client.
- **Load balancing and capacity:** Use multiple stateless application instances behind a load balancer as traffic requires. The estimates of 39 writes/sec and 3,900 reads/sec are averages, not enough to derive an exact server count; capacity testing and peak traffic assumptions are needed.
- **Caching:** Cache popular `short_code -> long_url` mappings. Show cache hits and misses, and decide how updates and expiration affect cached entries.
- **Redirect code:** A 302 temporary redirect is a reasonable default when destinations may change or browser caching should be limited. A 301 permanent redirect may be cached by browsers, making destination changes harder to propagate.
- **Data model:** At minimum store `short_code` (unique lookup key), `long_url`, creation time, and optional expiry/owner fields. User ID is only needed for ownership or link management.
- **Availability and abuse:** Consider database/read-replica failures, hot links, rate limits, and malicious destinations. Keep optional analytics work off the synchronous redirect path.

## Next revision checklist

- [ ] Draw create and redirect flows separately.
- [ ] Put CDN/cache on redirect path and show cache hit/miss behavior.
- [ ] Label API requests, database lookups/writes, and redirect response.
- [ ] State assumptions and identify functional and non-functional requirements.
- [ ] Explain database, ID generation, collision handling, idempotency, caching, and 301/302 choices.
- [ ] Describe autoscaling without claiming an unsupported fixed server count.
- [ ] Compare my design with the Primer's Pastebin/Bitly solution and record five concrete gaps.

## Reflection after comparison

1. Biggest gap:
2. Second gap:
3. Third gap:
4. Fourth gap:
5. Fifth gap:

