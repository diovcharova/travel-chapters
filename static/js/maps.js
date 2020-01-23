function initMap() {

  //initialize a geocoder and latmng object in order to intialize
  // a new map object
  let geocoder = new google.maps.Geocoder();
  let latlng = new google.maps.LatLng(46.619261, -33.134766);
  let map = new google.maps.Map(document.getElementById("map"), {
    zoom: 1,
    center: latlng
  });

  //make a call to the geocode function
  geocodeAddress(geocoder, map);

}
let labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let labelIndex = 0;

function geocodeAddress(geocoder, resultsMap) {
  let i;
  for (i = 0; i < document.getElementsByClassName('address').length; i++) {
    let address = document.getElementsByClassName('address')[i].textContent;
      //converts each address in the database to a geocode
    geocoder.geocode({ 'address': address }, function(results, status) {
      if (status === 'OK') {
        resultsMap.setCenter(results[0].geometry.location);
        // create a marker for each geocode that is returned successfully
        let marker = new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location,
          label: labels[labelIndex++ % labels.length],
        });
      }
    });
  }
}
