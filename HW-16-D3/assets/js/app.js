var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 30,
  right: 40,
  bottom: 70,
  left: 90,
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


// Select #scatter, append SVG area to it, and set the dimensions
var svg = d3.select("#scatter")
.append("svg")
.attr("width", svgWidth)
.attr("height", svgHeight);


// Append a group to the SVG area and shift ('translate') it to the right and down
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Import data from data.csv
d3.csv("assets/data/data.csv", function(error, data) {
  if (error) throw error;
 
  console.log(data);

  //Cast the values to numbers
  data.forEach(function(d) {
    d.poverty = +d.poverty;
    d.healthcare= +d.healthcare;
        
  });
  
//Create scale functions

var xLinearScale = d3.scaleLinear()
  .domain([d3.min(data, d => d.poverty)-0.5, d3.max(data, d => d.poverty)+0.5])
  .range([0, width]);

var yLinearScale = d3.scaleLinear()
  .domain([d3.min(data, d => d.healthcare)-1, d3.max(data, d => d.healthcare)+1.1])
  .range([height, 0]);
  
// Create axis functions
var bottomAxis = d3.axisBottom(xLinearScale);
var leftAxis = d3.axisLeft(yLinearScale);

//Append axes to the chart
chartGroup.append("g")
  .attr("transform", `translate(0, ${height})`)
  .call(bottomAxis);

chartGroup.append("g")
  .call(leftAxis);

//Create Circles
var circlesGroup = chartGroup.selectAll("circle").data(data).enter();
  
var cTip=circlesGroup.append("circle")  
  .classed("stateCircle", true)
  .attr("cx", d => xLinearScale(d.poverty))
  .attr("cy", d => yLinearScale(d.healthcare))
  .attr("r", "15")
  .attr("opacity", ".5");
  
//Create text labels with state abbreviation for each circle
circlesGroup.append("text")
  .classed("stateText", true)
  .attr("x", d => xLinearScale(d.poverty))
  .attr("y", d => yLinearScale(d.healthcare))
  .attr("stroke", "teal")
  .attr("font-size", "10px")
  .text(d => d.abbr)
    
  
//Initialize tool tip

var toolTip = d3.tip()
    .attr("class", "d3-tip")
    .offset([-8, 0])
    .html(function(d) {
      return (`${d.state}<br>Poverty: ${d.poverty}%<br>Healthcare: ${d.healthcare}%`);
  });

//Create tooltip in the chart
cTip.call(toolTip);

//Create event listeners to display and hide the tooltip
cTip.on("mouseover", function(d) {
  d3.select(this).style("stroke", "black")
  toolTip.show(d, this);
})
  //onmouseout event
  .on("mouseout", function(d, index) {
    d3.select(this).style("stroke", "lightblue")
    toolTip.hide(d);
  });

// Create axes labels
chartGroup.append("text")
.attr("transform", "rotate(-90)")
.attr("y", 0 - margin.left + 40)
.attr("x", 0 - (height / 2))
.attr("dy", "1em")
.attr("class", "aText")
.text("Lacks Healthcare (%)");

chartGroup.append("text")
.attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
.attr("class", "aText")
.text("In Poverty (%)");
    
});

    





