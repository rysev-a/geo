export interface MapLayer {
  id: number;
  name: string;
}

export interface MapElement {
  id: number;
  name: string;
  latitude: string;
  longitude: string;
  layer: MapLayer;
}
