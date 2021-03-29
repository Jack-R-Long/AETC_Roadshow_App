$(document).on("scroll", function(){

    if ($(document).scrollTop() > 80){
        $(".primary-nav").addClass("shrink");
    } else {
        $(".primary-nav").removeClass("shrink");
    }
    
});
$(document).ready(function() {
    console.log("ready!");

    $('#fileUpload').on('change', function () {
        // File upload and convert 
        var course_data = uploadCSV(this[0]);
        console.log(course_data);
        
        // Show in div
        $('#xmlOut').text(course_data);
    });
});

// nkotak's CSV to XML 
function CSVtoXML(csvData){
    // start xml output with blank variable xml
    var xml = `<?xml version="1.0"?>\n<tasks>\n`;
    // splits input CSV data values by lines, puts values into csvData
    var csvData = csvData.value.split("\n").map(row => row.trim());
    // gets XML header values from the 0th line which contains them
    var headers = csvData[0].split(",");
    // for loop which goes through data and starts to populate XML values
    for(var i=1;i<csvData.length;i++) {
        var values = csvData[i].split(",");
        xml += `<row${i}>\n`
        for (var j=0;j<headers.length;j++){
            xml += `<${headers[j]}>${values[j]}</${headers[j]}>`;
        }
        xml += `</row${i}>\n`
    }
    xml += `</tasks>`
    console.log(xml);
}
// function to upload CSV file directly to website
function uploadCSV(input){
    uploadedData = "";
    console.log("CHECK");
    console.log(input);
    // uses file reader to read file and put value into XML text area
    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function() {
      uploadedData.value = reader.result;
    };
    reader.onerror = function() {
      alert("Error reading file, fix file and try again.");
      return;
    };
    console.log("Uploaded CSV data");
    console.log(uploadedData);
    return uploadedData
  }