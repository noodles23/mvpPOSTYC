// queue()
//     // .defer(d3.csv)
//     .await(makeGraphs);

d3.csv('/static/demo_refunds.csv', function makeGraphs(data) {
	
//Start Transformations
	var dataSet =data ;
	// var dateFormat = d3.time.format("%m/%d/%Y");
	dataSet.forEach(function(d) {
		// d.month = dateFormat.parse(d.month);
				// d.transaction_date.setDate(1);
		d.date_requested_refund= +d.date_requested_refund;
		d.product_price = +d.product_price;
		d.refund_amtD = +d.refund_amtD;
		d.customer_preD = +d.customer_preD;
		d.customer_preC = +d.customer_preC;
		d.customer_postD = +d.customer_postD;
		d.customer_postC = +d.customer_postC;
		d.cs_prev_tickets = +d.cs_prev_tickets;
		d.cs_prev_cashD = +d.cs_prev_cashD;
		d.cs_prev_cashC = +d.cs_prev_cashC;
		d.cs_prev_creditD = +d.cs_prev_creditD;
		d.cs_prev_creditC = +d.cs_prev_creditC;
		d.customer_total_refunds = +d.customer_total_refunds;
		d.customer_total_refunds_count = +d.customer_total_refunds_count;
		d.customer_net_value = +d.customer_net_value;
		d.customer_gross_value = +d.customer_gross_value;
		d.customer_valueP = +d.customer_valueP;
		d.customer_last_active_fullmonths = +d.customer_last_active_fullmonths;
		d.customer_last_purchase_fullmonths = +d.customer_last_purchase_fullmonths;

	});

	//Create a Crossfilter instance
	var ndx = crossfilter(dataSet);

	//Define Dimensions
	var all = ndx.groupAll();	
	var monthNum = ndx.dimension(function(d) { return d.date_requested_refund; });
	var monthGroup = monthNum.group();


	var customerName = ndx.dimension(function(d) { return d.customer_name; });
	var customerGender = ndx.dimension(function(d) { return d.customer_gender; });
	var refundStatus = ndx.dimension(function(d) { return d.refund_status; });
	var refundType = ndx.dimension(function(d) { return d.refund_type; });
	var refundPartialFull = ndx.dimension(function(d) { return d.refund_partial_full; });
	var refundProdCategory = ndx.dimension(function(d) { return d.refund_product_category; });
	var refundReason = ndx.dimension(function(d) { return d.refund_reason; });
	var refundResponsibility = ndx.dimension(function(d) { return d.refund_responsibility; });
	var catrefundamt = ndx.dimension(function(d) { return d.refund_amt_cat; });
	var catpreviouspurchasecount = ndx.dimension(function(d) { return d.previous_purchase_cat; });
	var customerLost = ndx.dimension(function(d) { return d.customer_lost; });
	var customerPostStatus = ndx.dimension(function(d) { return d.post_status; });

//reduce by sum of total refunds
	var nameRefunds=customerName.group().reduceSum(dc.pluck('refund_amtD'));
	var refundsByMonth=monthNum.group().reduceSum(dc.pluck('refund_amtD'));
	var postTotal=customerPostStatus.group().reduceCount(dc.pluck('refund_amtD'));
	var futureSpendD=refundType.group().reduceSum(dc.pluck('customer_postD'));



//reduce by count
	var statusRefunds=refundStatus.group().reduceCount(dc.pluck('customer_name'));
	var genderRefunds=customerGender.group().reduceCount(dc.pluck('customer_name'));
	var typeRefunds=refundType.group().reduceCount(dc.pluck('customer_name'));
	var partialfullRefunds=refundPartialFull.group().reduceCount(dc.pluck('customer_name'));
	var prodcatRefunds=refundProdCategory.group().reduceCount(dc.pluck('customer_name'));
	var responseRefunds=refundResponsibility.group().reduceCount(dc.pluck('customer_name'));
	var reasonRefunds=refundReason.group().reduceCount(dc.pluck('customer_name'));
	var lostcRefunds=customerLost.group().reduceCount(dc.pluck('customer_name'));
	var catRefundAmt=catrefundamt.group().reduceCount(dc.pluck('customer_name'));
	var catPrevPurchaseGroup=catpreviouspurchasecount.group().reduceCount(dc.pluck('customer_name'));


//groups for all dimensions
	var groupName = customerName.group();
	var groupGender = customerGender.group();
	var groupRStatus = refundStatus.group();
	var groupRType = refundType.group();
	var groupRPF = refundPartialFull.group();
	var groupPCat = refundProdCategory.group();
	var groupRes = refundResponsibility.group();
	var groupCLost = customerLost.group();

	dc.dataCount("#row-selection")
        .dimension(ndx)
        .group(all);

        // priceDimension  = ndx.dimension(function(d) {return d.product_price; });
        // priceGroup = priceDimension.group().reduce(
        //     function (p, v) {
        //         ++p.count;
        //         p.sumPrice += v.price;
        //         p.avgPrice = p.sumPrice;
        //         return p;
        //     },
        //     function (p, v) {
        //         --p.count;
        //         p.sumPrice -= v.price;
        //         p.avgPrice = p.sumPrice;
        //         return p;
        //     },
        //     function () {
        //         return { count:0, sumPrice:0, avgPrice};
        //     });

	var postReturn=refundType.group().reduceSum(function(d) 
   {if (d.post_status==='Returned') {return +1;}else{return 0;}});
	var postLoss=refundType.group().reduceSum(function(d) 
   {if (d.post_status==='Lost') {return +1;}else{return 0;}});



	// var postCalcTotal=postReturn+postLoss);
	// var postRetPct=(postReturn/postCalcTotal*100);
	// var postLossPct=(postLoss/postCalcTotal*100);
   
 //   var salespriceByMonth=monthNum.group().reduceSum(dc.pluck('product_price'));
 //   var ordersByMonth=monthNum.group().reduceCount(dc.pluck('product_price'));
   

	var netTotalRefundsD = ndx.groupAll().reduceSum(dc.pluck('product_price'));
	var netTotalRefundsC = ndx.groupAll().reduceCount(dc.pluck('product_price'));

	//Define threshold values for data
	// var minDate = monthNum.bottom(1)[0].month;
	// var maxDate = monthNum.top(1)[0].month;


    //Charts
	// var netRefundsC = dc.numberDisplay("#total-refundsC");
	// var netRefundsD = dc.numberDisplay("#total-refundsD");
	var newcustChart = dc.lineChart("#newcust-chart");
	var testBChart = dc.barChart("#t1-chart");
	var postAvSpendD = dc.barChart("#t2-chart");
	// var postAvSpendP = dc.lineChart("#t3-chart");
	// var compositeChart1 = dc.compositeChart('#composite-chart');

	var selectRefundStatus = dc.pieChart("#p1-chart");
	var selectRefundType = dc.pieChart("#p2-chart");
	var selectPartialFull = dc.pieChart("#p3-chart");
	var selectProdCat = dc.pieChart("#p4-chart");
	var selectRefundReason = dc.pieChart("#p5-chart");
	var selectGender = dc.pieChart("#p6-chart");
	var selectRefundAmount = dc.pieChart("#p7-chart");
	var selectPreviousPurchases = dc.pieChart("#p8-chart");
	var selectCustomerActive = dc.pieChart("#p9-chart");

	var giantTable = dc.dataTable("#giantTable-chart");


	selectRefundStatus
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(refundStatus)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(statusRefunds);

 	selectRefundType
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(refundType)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(typeRefunds);
	
	selectPartialFull
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(refundPartialFull)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(partialfullRefunds);                

	selectProdCat
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(refundProdCategory)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(prodcatRefunds);

 	selectRefundReason
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(refundReason)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(reasonRefunds);
	
	selectGender
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(customerGender)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(genderRefunds);    

	selectRefundAmount
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(catrefundamt)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(catRefundAmt);

 	selectPreviousPurchases
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(catpreviouspurchasecount)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(catPrevPurchaseGroup);
	
	selectCustomerActive
            .height(150)
            //.width(350)
            .radius(75)
            .innerRadius(0)
            .transitionDuration(1000)
            .dimension(customerLost)
            .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
            .group(lostcRefunds);    



	// netRefundsC
	// 	.formatNumber(d3.format("d"))
	// 	.valueAccessor(function(d){return d; })
	// 	.group(netTotalRefundsC)
	// 	.formatNumber(d3.format(".3s"));

	// netRefundsD
	// 	.formatNumber(d3.format("d"))
	// 	.valueAccessor(function(d){return d; })
	// 	.group(netTotalRefundsD)
	// 	.formatNumber(d3.format(".3s"));

	newcustChart
		.width(500)
		.height(150)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(monthNum)
		.group(refundsByMonth,"Monthly Refunds ($)")
		.renderArea(true)
		.transitionDuration(500)
		.x(d3.scale.ordinal().domain(refundType))
		.x(d3.time.scale().domain([201501, 201512]))
		.elasticY(true)
		.renderHorizontalGridLines(true)
    	.renderVerticalGridLines(true)
		.xAxisLabel("2015 Month Number#")
		.legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
		.ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
		.yAxis().ticks(6);

	testBChart
		.width(400)
		.height(150)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(refundType)
		.group(postReturn,"Customers Returned")
		.stack(postLoss,"Customers Lost")
		// .renderArea(true)
		.transitionDuration(500)
		.x(d3.scale.ordinal().domain(refundType))
        .xUnits(dc.units.ordinal)
        .renderHorizontalGridLines(true)
        .renderVerticalGridLines(true)
        .ordering(function(d){return d.value;})
		.legend(dc.legend().x(150).y(10).itemHeight(13).gap(5))
		.ordinalColors(["#78CC00","#F8B700","#7B71C5"])
		.yAxis().ticks(6);


	postAvSpendD
		.width(400)
		.height(150)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(refundType)
		.group(futureSpendD,"Average Post Refund Spend ($)")
		// .renderArea(true)
		.transitionDuration(500)
		.x(d3.scale.ordinal().domain(refundType))
        .xUnits(dc.units.ordinal)
        .renderHorizontalGridLines(true)
        .renderVerticalGridLines(true)
        .ordering(function(d){return d.value;})
		.legend(dc.legend().x(150).y(10).itemHeight(13).gap(5))
		.ordinalColors(["#78CC00","#F8B700","#7B71C5"])
		.yAxis().ticks(6);

	giantTable.width(800).height(800)
    .dimension(customerName)
    .group(function(d) { return "Customer Name"
     })
    .size(100)
    .columns([
    	function(d) { return d.customer_name; },
        function(d) { return d.customer_id; },
        function(d) { return d.post_status; },
        function(d) { return '<a href="../">Select</a>'; }
    ])
    .sortBy(function(d){ return d.project_views; })
    // (optional) sort order, :default ascending
    .order(d3.descending);


	// var postAvSpendP = dc.lineChart("#t3-chart");
	// .group(postReturn,"Average Post Refund Spend % or refund amount")



	// compositeChart1
	// 	.width(500)
	// 	.height(300)
	// 	.margins({top: 10, right: 50, bottom: 30, left: 50});

			

    dc.renderAll();

});