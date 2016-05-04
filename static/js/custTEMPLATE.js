concat="/data/"+SearchTable + "/"+CustID;

queue()
    .defer(d3.json, concat)
    .await(makeGraphs);

function makeGraphs(error, data) {
	
//Start Transformations
	var dataSet =data;
	// var dateFormat = d3.time.format("%m/%d/%Y");
	dataSet.forEach(function(d) {
		// d.month = dateFormat.parse(d.month);
				// d.transaction_date.setDate(1);
		// d.touchpoint_month= +d.touchpoint_month;
		d.touchpoint_amount = +d.touchpoint_amount;
        d.touchpoint_count = +d.touchpoint_count;

	});

	//Create a Crossfilter instance
	var ndx = crossfilter(dataSet);

	//Define Dimensions
	var all = ndx.groupAll();	
	var monthNum = ndx.dimension(function(d) { return d.touchpoint_month; });
	var monthGroup = monthNum.group();

	var touchType = ndx.dimension(function(d) { return d.touchpoint_type; });
	var typeGroup = touchType.group();

	var touchSource = ndx.dimension(function(d) { return d.touchpoint_datasource; });
	var sourchGroup = touchSource.group();

	var custOnlySales=ndx.groupAll().reduceSum(function(d) 
   {if (d.touchpoint_owner==='yes') {return +d.touchpoint_amount;}else{return 0;}});

	
	var netTotalSales = ndx.groupAll().reduceSum(dc.pluck('touchpoint_amount'));
	var netTotalOrders = ndx.groupAll().reduceSum(dc.pluck('touchpoint_count'));


    //Charts
	var netOrders = dc.numberDisplay("#total-orders");
	var netSales = dc.numberDisplay("#total-sales");
	var custSales = dc.numberDisplay("#cust-sales");

	//NEED TO ADD A DATE CHART
	var giantTable = dc.dataTable("#giantTable-chart");


    selectField = dc.selectMenu('#menuMonth')
        .dimension(monthNum)
        .group(monthGroup); 

      selectField = dc.selectMenu('#menuPlatform')
        .dimension(touchSource)
        .group(sourchGroup); 

       selectField = dc.selectMenu('#menuType')
        .dimension(touchType)
        .group(typeGroup); 


        //add selectors for each touchpoint_type + touchpoint_name (for product names etc) + date value chart
    

    dc.dataCount("#row-selection")
        .dimension(ndx)
        .group(all);


	netOrders
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalOrders)
		.formatNumber(d3.format(""));

	netSales
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalSales)
		.formatNumber(d3.format("$.3s"));

	custSales
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(custOnlySales)
		.formatNumber(d3.format("$.3s"));


    giantTable.width(800).height(1000)
	    .dimension(monthNum)
	    .group(function(d) { return "Transaction Entry"
	     })
	    .size(100)
	    .columns([
	    	function(d) { return d.touchpoint_type; },
	        function(d) { return d.touchpoint_date; },
	        function(d) { return d.touchpoint_datasource; },
	        function(d) { return d.touchpoint_name; },
	        function(d) { return d.touchpoint_category; },
	        function(d) { return d.touchpoint_amount; }
	    ])
	    .sortBy(function(d){ return d.touchpoint_month; })
	    // (optional) sort order, :default ascending
	    .order(d3.ascending)
	        .renderlet(function (table) {
            $("#giantTable-chart tr").each(function (index, Element) {
                switch ($(Element).children("td").last().text()) {
                    case "purchase":
                        $(Element).css("background-color", "#FFFFCC");
                        break;
                    case "6":
                        $(Element).css("background-color", "#F5CCCC");
                        break;
                }
                if ($(Element).children("td").length > 1) {
                    $(Element).children("td").last().css("display", "none");
                }
            });
        });


    dc.renderAll();

};


