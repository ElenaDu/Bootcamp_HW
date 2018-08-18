const dataAr = dataSet


var tableBody=d3.select('#ufo_t').html("")

function makeTable(dataUfo) {
    var tableBody=d3.select('#ufo_t').html("")

    for (var i=0; i< dataUfo.length; i++) {
        var dataTr=tableBody.append("tr")
        dataTr.append('td').text(dataUfo[i].datetime)
        dataTr.append('td').text(dataUfo[i].city)
        dataTr.append('td').text(dataUfo[i].state)
        dataTr.append('td').text(dataUfo[i].country)
        dataTr.append('td').text(dataUfo[i].shape)
        dataTr.append('td').text(dataUfo[i].durationMinutes)
        dataTr.append('td').text(dataUfo[i].comments)
    }
    return(tableBody)
}

makeTable(dataAr)



var set1=dataSet

//Select the submit button
var submit=d3.select("#submit");

submit.on("click", function(){
    //prevent the page from refreshing
    d3.event.preventDefault();

    //select the input element and get the raw HTML node
    var inputElement = d3.select("#ufo-form-input");

    //get the value property of the input element
    var inputValue = inputElement.property("value");
    
    var filteredData =set1.filter(set => set.datetime===inputValue);
    
    makeTable(filteredData)


})


