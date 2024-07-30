$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
});

function sendAjaxRequest(url, data, successCallback) {
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: successCallback,
        error: function (xhr, status, error) {
            alert("An error occurred: " + error);
        }
    });
}

$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    sendAjaxRequest("/pluscart", { prod_id: id }, function(data) {
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.totalamount;
    });
});

$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    sendAjaxRequest("/minuscart", { prod_id: id }, function(data) {
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.totalamount;
    });
});

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this;
    sendAjaxRequest("/removecart", { prod_id: id }, function(data) {
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.totalamount;
        eml.parentNode.parentNode.parentNode.parentNode.remove();
    });
});

$('.plus-wishlist').click(function(){
    var id = $(this).attr("pid").toString();
    sendAjaxRequest("/pluswishlist", { prod_id: id }, function(data) {
        window.location.href = `http://localhost:8000/product-detail/${id}`;
    });
});

$('.minus-wishlist').click(function(){
    var id = $(this).attr("pid").toString();
    sendAjaxRequest("/minuswishlist", { prod_id: id }, function(data) {
        window.location.href = `http://localhost:8000/product-detail/${id}`;
    });
});
