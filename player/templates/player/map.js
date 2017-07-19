//
//
// var map_players = []
//
// "{% for player in players %}"
//   map_players.push( { username: "{{player.username}}", skill_level: "{{player.skill_level}}", address: "{{player.address}}", availability_days: "{{player.availability_days}}", availability_times: "{{player.availability_times}}", looking_for: "{{player.availability_days}}", phone_number: "{{player.phone_number}}", email: "{{player.email}}", additional_info: "{{player.additional_info}}" }, latitude: "{{player.latitude}}", longitude: "{{player.longitude}}")
// "{% endfor %}"
//
// // console.log(map_players)
// // var coordinates = {}
// // for (i = 0; i < map_players.length; i++) {
// //     for (i = 0; i < map_players.[i]["address"]; i ++) {
// //
// //     }
// // }
//
// console.log(map_players)
//
// function initMap() {
//
//
//   // var uluru = ; //this is the thing that moves the marker
//   // var seattle = {}//{lat: 47.608013, lng: -122.335167};
//   var map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 4,
//     center: {lat: 47.608013, lng: -122.335167}
//   });
//   var marker = new google.maps.Marker({
//     // position: uluru,
//     position: {lat: 47.608013, lng: -122.335167},
//     map: map
//   });
//
//   var new_marker = new google.maps.Marker({
//     position: {lat: -30.363, lng: 140.044},
//     map: map
//   });
// }
// </script>
//
// <script async defer
// src="https://maps.googleapis.com/maps/api/js?key={{GOOGLE_API_KEY}}&callback=initMap">
