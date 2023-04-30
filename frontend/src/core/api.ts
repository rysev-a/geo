import axios from "axios";

const api = {
  loadSchools: () => axios.get("/api/schools/schools"),
};

export default api;
