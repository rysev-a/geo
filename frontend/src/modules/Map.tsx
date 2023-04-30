import { useEffect, useState } from "react";
import api from "core/api.ts";

import { MapElement } from "modules/config.ts";
import { fromLonLat } from "ol/proj.js";

const MapView = () => {
  const [elements, setElements] = useState([]);

  useEffect(() => {
    api.loadElements().then((response) => {
      setElements(response.data.results);
      loadMap2(response.data.results);
    });
  }, []);

  return (
    <div className="container my-5">
      <h1>Map</h1>

      <div className="row">
        <div className="col-6">
          <div className="card">
            <table className="table small">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">name</th>
                  <th scope="col">latitude</th>
                  <th scope="col">longitude</th>
                </tr>
              </thead>
              <tbody>
                {elements.map((element: MapElement) => {
                  return (
                    <tr key={element.id}>
                      <th scope="row">{element.id}</th>
                      <td>{element.name}</td>
                      <td>{element.latitude}</td>
                      <td>{element.longitude}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
        <div className="col-6">
          <div className="map" id="map"></div>
        </div>
      </div>
    </div>
  );
};

import Feature from "ol/Feature.js";
import Map from "ol/Map.js";
import View from "ol/View.js";
import { Circle } from "ol/geom.js";
import { OSM, Vector as VectorSource } from "ol/source.js";
import { Style } from "ol/style.js";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer.js";

function loadMap2(elements: MapElement[]) {
  const drawCircle = (mapElement: MapElement) => {
    const circleFeature = new Feature({
      geometry: new Circle(
        fromLonLat([Number(mapElement.longitude), Number(mapElement.latitude)]),
        500
      ),
    });

    circleFeature.setStyle(
      new Style({
        renderer(coordinates, state) {
          const [[x, y], [x1, y1]] = coordinates;
          const ctx = state.context;
          const dx = x1 - x;
          const dy = y1 - y;
          const radius = Math.sqrt(dx * dx + dy * dy);

          const innerRadius = 0;
          const outerRadius = radius * 1.4;

          const gradient = ctx.createRadialGradient(
            x,
            y,
            innerRadius,
            x,
            y,
            outerRadius
          );
          gradient.addColorStop(0, "rgba(255,0,0,0)");
          gradient.addColorStop(0.6, "rgba(255,0,0,0.2)");
          gradient.addColorStop(1, "rgba(255,0,0,0.8)");
          ctx.beginPath();
          ctx.arc(x, y, radius, 0, 2 * Math.PI, true);
          ctx.fillStyle = gradient;
          ctx.fill();

          ctx.arc(x, y, radius, 0, 2 * Math.PI, true);
          ctx.strokeStyle = "rgba(255,0,0,1)";
          ctx.stroke();
        },
      })
    );

    return circleFeature;
  };

  const features = elements.map((element: MapElement) => {
    return drawCircle(element);
  });

  new Map({
    layers: [
      new TileLayer({
        source: new OSM(),
        visible: true,
      }),
      new VectorLayer({
        source: new VectorSource({
          features: features,
        }),
      }),
    ],
    target: "map",
    view: new View({
      // center: [12127398.797692968, 4063894.123105166],
      center: fromLonLat([elements[1].longitude, elements[1].latitude]),
      zoom: 14,
    }),
  });
}

export default MapView;
