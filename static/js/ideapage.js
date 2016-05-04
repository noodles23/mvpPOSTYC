// queue()
//     // .defer(d3.csv)
//     .await(makeGraphs);

d3.csv('/static/uptomanhat2.csv', function makeGraphs(data) {
	
//Start Transformations
	var dataSet =data ;
	// var dateFormat = d3.time.format("%m/%d/%Y");
	dataSet.forEach(function(d) {
		// d.month = dateFormat.parse(d.month);
				// d.transaction_date.setDate(1);
		d.month= +d.month;
		d.project_views = +d.project_views;

	});

	//Create a Crossfilter instance
	var ndx = crossfilter(dataSet);

	//Define Dimensions
	var all = ndx.groupAll();	
	var monthNum = ndx.dimension(function(d) { return d.month; });
	var hacksource = ndx.dimension(function(d) { return d.source_hackathon; });
	var projectname = ndx.dimension(function(d) { return d.project_name; });
	var techSpread = ndx.dimension(function(d) { return d.tPrimary; });
	var catSpread = ndx.dimension(function(d) { return d.project_category; });
	var typeSpread = ndx.dimension(function(d) { return d.project_type; });


	var sourceGroup = hacksource.group();
	var techGroup = techSpread.group();
	var catGroup = catSpread.group();
	var typeGroup = typeSpread.group();


	// var lRuby=monthNum.group().reduceCount(function(d) 
 //   {if (d.tRuby==='TRUE') {return +d.project_views;}else{return 0;}});
	// var lJava=monthNum.group().reduceCount(function(d) 
 //   {if (d.tJava==='TRUE') {return +d.project_views;}else{return 0;}});
	// var lCsharp=monthNum.group().reduceCount(function(d) 
 //   {if (d.TC#==='TRUE') {return +d.project_views;}else{return 0;}});
	// var lPython=monthNum.group().reduceCount(function(d) 
 //   {if (d.TPython==='TRUE') {return +d.project_views;}else{return 0;}});
	// var lPhp=monthNum.group().reduceCount(function(d) 
 //   {if (d.TPhp==='TRUE') {return +d.project_views;}else{return 0;}});
	// var lJs=monthNum.group().reduceCount(function(d) 
 //   {if (d.TJavascript==='TRUE') {return +d.project_views;}else{return 0;}});

	var netTotalProjects = ndx.groupAll().reduceCount(dc.pluck('project_name'));
	var netTotalViews = ndx.groupAll().reduceSum(dc.pluck('project_views'));
	var viewsbyTech=techSpread.group().reduceCount(dc.pluck('project_views'));
	var viewsbyCat=catSpread.group().reduceCount(dc.pluck('project_views'));
	var viewsbyType=typeSpread.group().reduceCount(dc.pluck('project_views'));


	//Define threshold values for data
	var minDate = monthNum.bottom(1)[0].month;
	var maxDate = monthNum.top(1)[0].month;

    //Charts
	var netProjects = dc.numberDisplay("#total-Projects");
	var netViews = dc.numberDisplay("#total-Views");
	var techP = dc.pieChart("#techPie-chart");
	var catP = dc.pieChart("#catPie-chart");
	var typeP = dc.pieChart("#typePie-chart");
	var giantTable = dc.dataTable("#giantTable-chart");

	selectField = dc.selectMenu('#menuselect')
        .dimension(hacksource)
        .group(sourceGroup); 

    selectField = dc.selectMenu('#menuselect2')
        .dimension(catSpread)
        .group(catGroup); 

    selectField = dc.selectMenu('#menuselect3')
        .dimension(typeSpread)
        .group(typeGroup); 

    dc.dataCount("#row-selection")
        .dimension(ndx)
        .group(all);


	netProjects
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalProjects)
		.formatNumber(d3.format(".3s"));

	netViews
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(netTotalViews)
		.formatNumber(d3.format(".3s"));

	techP
            .height(350)
            .width(500)
            .radius(150)
            .innerRadius(50)
            .transitionDuration(1000)
            .dimension(techSpread)
            .ordinalColors(["#B26480","#FFF265","#FF2672","#17A8CC","#B2A730", "#2CCC65"])
            .legend(dc.legend().x(0).y(0).gap(5))
            .group(viewsbyTech);

    	catP
            .height(350)
            .width(500)
            .radius(150)
            .innerRadius(50)
            .transitionDuration(1000)
            .dimension(catSpread)
            .ordinalColors(["#B26480","#FFF265","#FF2672","#17A8CC","#B2A730", "#2CCC65"])
            .legend(dc.legend().x(0).y(0).gap(5))
            .group(viewsbyCat);


       typeP
            .height(350)
            .width(500)
            .radius(150)
            .innerRadius(50)
            .transitionDuration(1000)
            .dimension(typeSpread)
            .ordinalColors(["#B26480","#FFF265","#FF2672","#17A8CC","#B2A730", "#2CCC65"])
            .legend(dc.legend().x(0).y(0).gap(5))
            .group(viewsbyType);

 

    giantTable.width(800).height(800)
    .dimension(projectname)
    .group(function(d) { return "Project Name"
     })
    .size(100)
    .columns([
    	function(d) { return d.project_name; },
        function(d) { return d.project_views; },
        function(d) { return d.project_technology; },
        function(d) { return d.project_description; },
        function(d) { return '<a href="../">Select</a>'; }
    ])
    .sortBy(function(d){ return d.project_views; })
    // (optional) sort order, :default ascending
    .order(d3.descending);


    dc.renderAll();

});