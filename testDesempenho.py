from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    # def on_start(self):
    #     self.client.post("/login", json={"email":"teste@gmail.com",
    #                                     "password":"12345678"})

    @task
    def home(self):
        self.client.get("/api/despesasTest")

    # @task
    # def root(self):
    #     self.client.get("/")