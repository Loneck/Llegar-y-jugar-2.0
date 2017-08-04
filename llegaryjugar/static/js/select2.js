$(".js-data-example-ajax").select2({
  ajax: {
    url: '/reservation/api/v1/schedule/',
    dataType: 'json',
    delay: 250,
    processResults: function(data, params) {
      var i;
      var location;
      var results = [];
      for (i = 0; i < data.length; i += 1) {
        location = data[i];
        results.push({
          id: location.id,
          text: location.court
        });
      }
      return {
        results: results
      };
    },
    cache: true
  },
  width: '100%',
});