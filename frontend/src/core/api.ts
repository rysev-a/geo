import axios from "axios";

const api = {
  loadElements: () => axios.get("/api/map/elements"),
};

export default api;
