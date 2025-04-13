let map;
let markers = [];

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 24.1477, lng: 120.6736 },
    zoom: 15,
  });
}

function clearMarkers() {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
}

function drawMarkers(center, parkingData) {
  map.setCenter(center);
  clearMarkers();

  parkingData.forEach(p => {
    const marker = new google.maps.Marker({
      position: { lat: p.lat, lng: p.lng },
      map: map,
      title: `${p.name} (${p.surplus} 空位)`,
      icon: p.surplus > 0 ? "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
                         : "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
    });
    markers.push(marker);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initMap();
  const btn = document.getElementById("searchBtn");

  btn.addEventListener("click", async () => {
    const keyword = document.getElementById("searchBox").value;
    if (!keyword) return alert("請輸入地點名稱");

    try {
      const res = await fetch(`https://your-render-api.onrender.com/query?keyword=${encodeURIComponent(keyword)}`);
      const data = await res.json();

      if (data.error) return alert(data.error);
      drawMarkers(data.center, data.parking);
    } catch (err) {
      console.error("查詢失敗", err);
      alert("查詢過程發生錯誤");
    }
  });
});