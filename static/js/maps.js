function initMap() {
  let geocoder = new google.maps.Geocoder();
  let latlng = new google.maps.LatLng(46.619261, -33.134766);
  let map = new google.maps.Map(document.getElementById("map"), {
    zoom: 1,
    center: latlng
  });
  geocodeAddress(geocoder, map);

}
let labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let labelIndex = 0;

function geocodeAddress(geocoder, resultsMap) {
  let i;
  for (i = 0; i < document.getElementsByClassName('address').length; i++) {
    let address = document.getElementsByClassName('address')[i].textContent;
    geocoder.geocode({ 'address': address }, function(results, status) {
      if (status === 'OK') {
        resultsMap.setCenter(results[0].geometry.location);
        let marker = new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location,
          label: labels[labelIndex++ % labels.length],
        });
      }
    });
  }
}
