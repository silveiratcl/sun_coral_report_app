const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> Sun Coral Report";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map.
    locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([-48.37, -26.28], 5));

async function load_markers() {
    const markers_url = `/api/markers/markers/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(markers_url)
    const geojson = await response.json()
    return geojson
}

async function render_markers() {
    const markers = await load_markers();
    L.geoJSON(markers)
    /*.bindPopup((layer) => layer.feature.properties.name)*/
    .bindPopup((layer) => '<img src="'+layer.feature.properties.image+'" /><p>'+layer.feature.properties.name+'</p>')
    .addTo(map);
}

map.on("moveend", render_markers);

/*layer.bindPopup('<img src="'+feature.properties.photo+'" /><p>'+feature.properties.name+'</p>');*/