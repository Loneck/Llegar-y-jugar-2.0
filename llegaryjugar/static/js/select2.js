var courtId;
$("#id_1-court").on("change", function(){
  courtId = $(this).val();
  console.log("this is the court id: " + courtId);
  loadSchedules(courtId);
});

$("#id_1-date").datepicker({
  format: "yyyy-mm-dd"
});


function loadSchedules(courtId) {
  var date = $('#id_1-date').val();
  console.log("la fecha qla!!" + date);
    $("#id_1-schedule").select2({
    ajax: {
      url: "/reservation/api/v1/schedule/?court=" + courtId + "&date=" + date,
      dataType: "json",
      delay: 250,
      processResults: function(data, params) {
        var i;
        var location;
        var results = [];
        for (i = 0; i < data.length; i += 1) {
          location = data[i];
          var text = location.id + ' ' + location.court;
          results.push({
            id: location.id,
            text: text
          });
        }
        return {
          results: results
        };
      },
      cache: true
    },
    width: "100%",
  })
};