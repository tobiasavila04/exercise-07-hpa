from locust import HttpUser, task

class NodeRegistryUser(HttpUser):
    @task
    def health(self):
        self.client.get("/health")

    @task
    def list_nodes(self):
        self.client.get("/api/nodes")
