from p1_validate import validate
class TestValidate:
    def test_validate_bad_amount(self):
        r,e=validate({"order_id":"1","customer_id":"1","amount":"-1","order_date":"2026-10-05"})
        assert r is None
        assert e == ["amount must be numeric and at least 0"]

    def test_validate_bad_date(self):
            r,e=validate({"order_id":"1","customer_id":"1","amount":"1","order_date":"2026/10/05T20:32:00Z"})
            assert r is None
            assert e == ["order_date must be a valid ISO date"]

    def test_validate_missing_customer(self):
            r,e=validate({"order_id":"1","amount":"1","order_date":"2026-10-05"})
            assert r is None
            assert e == ["customer_id must be non-empty"]

    def test_validate_valid_row(self):
            r,e=validate({"order_id":"1","customer_id":"1","amount":"1","order_date":"2026-10-05"})
            assert r == {"order_id":1,"customer_id":"1","amount":1.0,"order_date":"2026-10-05"}
            assert e is None

