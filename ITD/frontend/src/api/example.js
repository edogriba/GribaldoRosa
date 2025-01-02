import { Method } from "./api";
import { request } from "./request";

const resource = "/example";

export const example = async (resourceId) =>
  request(`${resource}/${resourceId}`, Method.GET, null, { limit: 10 });
