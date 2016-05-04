// queue()
//     // .defer(d3.csv)
//     .await(makeGraphs);

d3.csv('/static/demo_cust_base.csv', function makeGraphs(data) {
	
//Start Transformations
	var dataSet =data ;
	// var dateFormat = d3.time.format("%m/%d/%Y");
	dataSet.forEach(function(d) {
		// d.month = dateFormat.parse(d.month);
				// d.transaction_date.setDate(1);
		d.month= +d.month;
		d.product_price = +d.product_price;
	});

	//Create a Crossfilter instance
	var ndx = crossfilter(dataSet);

	//Define Dimensions
	var all = ndx.groupAll();	
	var monthNum = ndx.dimension(function(d) { return d.month; });
	var monthGroup = monthNum.group();

	var customerName = ndx.dimension(function(d) { return d.customer_name; });

	var custStatus = ndx.dimension(function(d) { return d.customer_new_or_return; });
	var statusGroup = custStatus.group();
	
	var prodCategory = ndx.dimension(function(d) { return d.product_category; });
	var prodGroup = prodCategory.group();

	var prodName = ndx.dimension(function(d) { return d.product_name; });
	var nameGroup = prodName.group();

	var genderStatus = ndx.dimension(function(d) { return d.customer_gender; });
	var genderGroup = genderStatus.group();

    var custSales=customerName.group().reduceSum(dc.pluck('product_price'));

        priceDimension  = ndx.dimension(function(d) {return d.product_price; });
        priceGroup = priceDimension.group().reduce(
            function (p, v) {
                ++p.count;
                p.sumPrice += v.price;
                p.avgPrice = p.sumPrice;
                return p;
            },
            function (p, v) {
                --p.count;
                p.sumPrice -= v.price;
                p.avgPrice = p.sumPrice;
                return p;
            },
            function () {
                return { count:0, sumPrice:0, avgPrice};
            });

	var custNew=monthNum.group().reduceSum(function(d) 
   {if (d.customer_new_or_return==='new') {return +1;}else{return 0;}});
	var custReturn=monthNum.group().reduceSum(function(d) 
   {if (d.customer_new_or_return==='return') {return +1;}else{return 0;}});
   
   var salespriceByMonth=monthNum.group().reduceSum(dc.pluck('product_price'));
   var ordersByMonth=monthNum.group().reduceCount(dc.pluck('product_price'));
   
   	var custCity = ndx.dimension(function(d) { return d.customer_state; });
	var cityGroup = custCity.group();
	
	var netTotalSales = ndx.groupAll().reduceSum(dc.pluck('product_price'));
	var netTotalOrders = ndx.groupAll().reduceCount(dc.pluck('product_price'));

	//Define threshold values for data
	var minDate = monthNum.bottom(1)[0].month;
	var maxDate = monthNum.top(1)[0].month;


    //Charts
	var netOrders = dc.numberDisplay("#total-orders");
	var netSales = dc.numberDisplay("#total-sales");
	var newcustChart = dc.lineChart("#newcust-chart");
	var topcustchart = dc.rowChart("#topcust-chart");



	selectField = dc.selectMenu('#menuState')
        .dimension(custCity)
        .group(cityGroup); 

    selectField = dc.selectMenu('#menuGender')
        .dimension(genderStatus)
        .group(genderGroup); 

    selectField = dc.selectMenu('#menuProdCat')
        .dimension(prodCategory)
        .group(prodGroup); 

    selectField = dc.selectMenu('#menuselect')
        .dimension(custCity)
        .group(cityGroup); 

    selectField = dc.selectMenu('#menuProdName')
        .dimension(prodName)
        .group(nameGroup); 

    selectField = dc.selectMenu('#menuStatus')
        .dimension(custStatus)
        .group(statusGroup); 

    dc.dataCount("#row-selection")
        .dimension(ndx)
        .group(all);


	netOrders
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalOrders)
		.formatNumber(d3.format(".3s"));

	netSales
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalSales)
		.formatNumber(d3.format(".3s"));

	newcustChart
		.width(700)
		.height(300)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(monthNum)
		.group(custReturn, 'Loss Rate Before')
		.stack(custNew,'Loss Rate After')
		.renderArea(true)
		.transitionDuration(500)
		.x(d3.time.scale().domain([minDate, maxDate]))
		.elasticY(true)
		.renderHorizontalGridLines(true)
    	.renderVerticalGridLines(true)
		.xAxisLabel("Month")
		.legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
		.elasticX(true)
        // .brushOn(false)
        .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
		.yAxis().ticks(6);	

    topcustchart
    .width(1000)
    .height(700)
    .margins({top: 5, left: 10, right: 10, bottom: 20})
    .dimension(customerName)
    .group(custSales)
    .colors(d3.scale.category10())
    .elasticX(true)
    .rowsCap(25)
    .ordering(function(d){ return d.value.avgPrice})
    .othersGrouper(false)
    .xAxis().ticks(4);

    dc.renderAll();

});