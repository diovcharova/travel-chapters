function initMap() {
    var geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(46.619261, -33.134766);
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 1,
      center: latlng
    });
    geocodeAddress(geocoder, map);
  }
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var labelIndex = 0;

  function geocodeAddress(geocoder, resultsMap) {
    var i;
    for (i = 0; i < document.getElementsByClassName('address').length; i++) {
      var address = document.getElementsByClassName('address')[i].textContent;
      geocoder.geocode({ 'address': address }, function(results, status) {
        if (status === 'OK') {
          resultsMap.setCenter(results[0].geometry.location);
          var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location,
            label: labels[labelIndex++ % labels.length],
          });
        }
        else {
          alert('Geocode was not successful for the following reason: ' + status);
        }
      });
    }
  }
