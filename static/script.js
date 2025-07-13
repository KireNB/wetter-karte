const map = L.map('map').setView([52.52, 13.41], 5); // Start: Berlin

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap',
}).addTo(map);

let marker;

map.on('click', function (e) {
    const { lat, lng } = e.latlng;

    if (marker) map.removeLayer(marker);
    marker = L.marker([lat, lng]).addTo(map);

    fetch(`/api/wetter?lat=${lat}&lon=${lng}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) return;

            document.getElementById("ort").innerText = `Wetter für ${lat.toFixed(2)}, ${lng.toFixed(2)}`;

            let html = `
                <table>
                    <tr><th>Datum</th><th>Max Temperatur (°C)</th></tr>
                    ${data.map(row => `<tr><td>${row.datum}</td><td>${row.temp}</td></tr>`).join("")}
                </table>
            `;

            document.getElementById("wetter").innerHTML = html;
        });
});
