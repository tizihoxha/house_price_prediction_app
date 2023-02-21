
//make post request for prediction
function onClickedEstimatePrice() {
    console.log("Clicked Estimate Price Button");
    var sqft = document.getElementById("uiSqtf");
    var Bedrooms = document.getElementById("uiBedrooms");
    var Bathrooms = document.getElementById("uiBathrooms");
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "/api/predict_home_price";

    $.post(url, {
        sqft: parseFloat(sqft.value),
        bedrooms: parseInt(Bedrooms.value),
        bathrooms: parseFloat(Bathrooms.value),
        location: location.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h4>" + data.estimated_price.toString() + " $</h4>";
        console.log(status);
    });
}
//poplating the dropdown menu for property locations

function onPageLoad() {
    console.log("loaded document");
    var url = "/api/locations";
    $.get(url, function(data, status) {
        console.log("received response from get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
                console.log(status)
            }
        }
    });
}

window.onload = onPageLoad;