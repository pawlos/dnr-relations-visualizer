var barWidth = 10,
    height = 500;


d3.json("episodes.json", function(error, data) {
  var max = d3.max(data, function(d) { return d.episodeLen; }) + 50;

  var width = barWidth * data.length
  var x = d3.scale.ordinal()
    .range([0, width]);

  var y = d3.scale.linear()
    .range([height, 0]);

  var chart = d3.select(".episodeLengthChart")
    .attr("width", width)
    .attr("height", height);
  
  y.domain([0, max]);
  x.range([0, width]);

    var avg = d3.mean(data, function(d) { return +d.episodeLen; });

  var bar = chart.selectAll("g")
      .data(data)
    .enter().append("g")
      .attr("transform", function(d, i) { return "translate("+i * barWidth+", 0)"; });

  chart.append("text")
      .attr("y", 25)
      .text(function(d) { return "Average episode length: "+avg.toFixed(2) + " minutes"})

  bar.append("rect")
      .attr("y", function(d) { return y(d.episodeLen); })
      .attr("height", function(d) { return height - y(d.episodeLen); })
      .style("stroke","white")
      .style("fill","blue")
      .attr("width", barWidth - 1);

  bar.append("text")
      .attr("y", function(d) { return y(d.episodeLen) - 10; })
      .attr("dy", ".75em")
      .style("font-size","10px")
      .style("fill", "black")
      .text(function(d) { return d.episodeLen; });

  bar.append("text")
      .attr("y", function(d) { return height;})
      .attr("transform", function(d) { return "rotate(-90)"; })
      .style("font-size","10px")
      .text(function (d) { return d.no })

    
  chart.append("line")
    .attr("x1", 0)
    .attr("y1", (1 - (avg/max))*height)
    .attr("x2", width)
    .attr("y2", (1 - (avg/max))*height)
    .style("stroke","red");


  var minMaxChart = d3.select(".minMaxChart")
                      .attr("width",500)
                      .attr("height", 200);

  var min = d3.min(data, function(d) { return +d.episodeLen == 0 ? Number.MAX_VALUE : +d.episodeLen; });
  var max = d3.max(data, function(d) { return +d.episodeLen; });

  minMaxChart.append("text")
          .attr("y", 25)
          .text(function(d) { return "Shortest(*) episode: "+min+" minutes." });
  minMaxChart.append("text")
          .attr("y", 50)
          .text(function(d) { return "Longest episode: " + max + " minutes." });

  minMaxChart.append("text")
          .attr("y", 75)
          .text(function(d) { return "* - excluding wrongly marked as 0 minutes episodes" });
});