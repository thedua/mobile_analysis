window.onload = function () {

  var token = $('input[name=csrfmiddlewaretoken]').val();

  $.ajax({
    type: "POST",
    url: "/getMobileData/",
    data: {
        csrfmiddlewaretoken: token,
        slug: slug
    },
    success: function(data) {
          list = []
					for(key in data){
            var i = 0;
            var temp = {};
            if(key=='high'){
              temp['exploded'] = true
            }
            for(val in data[key]){
              if(i==0){
                temp['y'] = data[key][val];
                i = 1;
              }else{
                temp['name'] = data[key][val];
              }
            }
            list.push(temp)
					}

          var chart = new CanvasJS.Chart("chartContainer", {
          	exportEnabled: true,
          	animationEnabled: true,

          	legend:{
          		cursor: "pointer",
          		itemclick: explodePie
          	},
          	data: [{
          		type: "pie",
          		showInLegend: true,
          		toolTipContent: "{name}: <strong>{y}%</strong>",
          		indexLabel: "{name} - {y}%",
          		dataPoints: list
          	}]
          });
          chart.render();

    },
    error: function(ts) {
          alert(ts.responseText)
    }
  });


  $.ajax({
    type: "POST",
    url: "/getMobileCameraData/",
    data: {
        csrfmiddlewaretoken: token,
        slug: slug
    },
    success: function(data) {
          list = []
          for(key in data){
            var i = 0;
            var temp = {};
            for(val in data[key]){
              if(i==0){
                temp['y'] = data[key][val];
                i = 1;
              }else{
                temp['label'] = data[key][val];
              }
            }
            list.push(temp)
          }


          var camera = new CanvasJS.Chart("cameraAnalysis", {
            	animationEnabled: true,
            	data: [{
            		type: "doughnut",
            		startAngle: 60,
            		//innerRadius: 60,
            		indexLabelFontSize: 12,
            		indexLabel: "{label} - #percent%",
            		toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            		dataPoints: list
            	}]
            });
            camera.render();

    },
    error: function(ts) {
          alert(ts.responseText)
    }
  });


  $.ajax({
    type: "POST",
    url: "/getMobileBatteryData/",
    data: {
        csrfmiddlewaretoken: token,
        slug: slug
    },
    success: function(data) {
          list = []
          for(key in data){
            var i = 0;
            var temp = {};
            for(val in data[key]){
              if(i==0){
                temp['y'] = data[key][val];
                i = 1;
              }else{
                temp['label'] = data[key][val];
              }
            }
            list.push(temp)
          }


          var battery = new CanvasJS.Chart("batteryAnalysis", {
            	animationEnabled: true,
            	data: [{
            		type: "doughnut",
            		startAngle: 60,
            		//innerRadius: 60,
            		indexLabelFontSize: 12,
            		indexLabel: "{label} - #percent%",
            		toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            		dataPoints: list
            	}]
            });
            battery.render();

    },
    error: function(ts) {
          alert(ts.responseText)
    }
  });


  $.ajax({
    type: "POST",
    url: "/getMobileMemoryData/",
    data: {
        csrfmiddlewaretoken: token,
        slug: slug
    },
    success: function(data) {
          list = []
          for(key in data){
            var i = 0;
            var temp = {};
            for(val in data[key]){
              if(i==0){
                temp['y'] = data[key][val];
                i = 1;
              }else{
                temp['label'] = data[key][val];
              }
            }
            list.push(temp)
          }


          var memory = new CanvasJS.Chart("memoryAnalysis", {
            	animationEnabled: true,
            	data: [{
            		type: "doughnut",
            		startAngle: 60,
            		//innerRadius: 60,
            		indexLabelFontSize: 12,
            		indexLabel: "{label} - #percent%",
            		toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            		dataPoints: list
            	}]
            });
            memory.render();

    },
    error: function(ts) {
          alert(ts.responseText)
    }
  });



}

function explodePie (e) {
	if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();

}
