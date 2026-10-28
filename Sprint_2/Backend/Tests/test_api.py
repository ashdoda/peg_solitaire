from app import app


def setup_method(self=None):
    pass


class TestApi:
    def setup_method(self):
        self.client = app.test_client()
        self.client.post("/api/new-game",
                         json={"size": "7", "boardType": "english"})

    def test_new_game_returns_board(self):
        response = self.client.post(
            "/api/new-game", json={"size": "9", "boardType": "diamond"})
        assert response.status_code == 200
        assert response.get_json()["size"] == 9

    def test_bad_size_returns_400_and_keeps_game(self):
        response = self.client.post(
            "/api/new-game", json={"size": "8", "boardType": "english"})
        assert response.status_code == 400
        assert self.client.get("/api/state").get_json()["size"] == 7

    def test_valid_and_invalid_move(self):
        ok = self.client.post("/api/move", json={
            "fromRow": 3, "fromCol": 1, "toRow": 3, "toCol": 3})
        assert ok.get_json()["valid"] is True
        bad = self.client.post("/api/move", json={
            "fromRow": 3, "fromCol": 1, "toRow": 3, "toCol": 3})
        assert bad.get_json()["valid"] is False