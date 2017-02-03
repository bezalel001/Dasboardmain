var app = angular.module('cpdApp', ['ngRoute']);

'use strict';

/* Controllers */
google.load('visualization', '1', {
  packages: ['corechart']
});

google.setOnLoadCallback(function() {
  angular.bootstrap(document.body, ['cpdApp']);
});


// app.config(['$routeProvider', 
// 	function($routeProvider){
// 		$routeProvider
// 		.when('/cpdashboard/', {
// 			templateUrl: 'static/cpdashboard/app/partials/initiative-detail.html',
// 			controller: MyCtrl1
// 		});
// 	}]);
// app.config(['$httpProvider', 
// 	function($httpProvider){
// 		$httpProvider.defaults.xsrfCookieName ='csrftoken';
// 		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
// 	}]);

    	
app.controller('CostController', ['$scope', '$http', function($scope, $http) {
	b = 1;
	p = 1;
	
    $http.get("/cpdashboard/inits/" + initiative.id + "/?format=json")
    .success(function(data) {
    	myData(data);
        // console.log(b);
    });
    
    function myData(data){

    	b = data.budgeted_cost;
    	p = data.projected_end_cost;
      ac = data.actual_cost;
      console.log(ac);
        $scope.initiative = data;
        $scope.budget = data.budgeted_cost;
        $scope.statuscode = data.status;
        $scope.statustext = data.statusText; 


        var data = new google.visualization.DataTable(
   {
     cols: [{id: 'p', label: 'Parameter', type: 'string'},
            {id: 'bud', label: 'Budgeted Cost', type: 'number'},
            {id: 'est', label: 'Estimated Cost at Completion', type: 'number'},
            {id: 'ac', label: 'Actual Cost', type: 'number'}],
     rows: [{c:[{v: 'Cost'}, {v: b},{v: p}, {v: p}, {v: ac}]}, ]
   }
 );
//     var data = google.visualization.arrayToDataTable([
//         ['Parameter', 'Budget', 'Estimate'],
//         ['Cost', {v: b},{v: p}]
//          ]);

      var options = {
        // title: 'Project\'s Cost Performance',
        curveType: 'function',
        legend: { position: 'top', alignment: 'end' },
        // colors: ['#e0440e', '#e6693e', '#ec8f6e', '#f3b49f', '#f6c7b6'],
        is3D: true
      };
      var chart = new google.visualization.BarChart(document.getElementById('cost'));


      chart.draw(data, options);
       $(window).resize(function(){
	   chart.draw(data, options);
	});
       
    }
     

    
}]);

app.controller('ScheduleController', ['$scope', '$http', function($scope, $http) {
	b = 1;
	p = 1;
	
    $http.get("/cpdashboard/inits/" + initiative.id + "/?format=json")
    .success(function(data) {
    	myData(data);
        // console.log(b);
    });
    
    function myData(data){

    	//a = data.scheduled_start_date;
    	//b = data.actual_start_date;
    	c = data.scheduled_end_date;
    	d = data.projected_end_date;
        $scope.initiative = data;
        
        $scope.statuscode = data.status;
        $scope.statustext = data.statusText; 

        sed = function(date){
        	var mydate = date.split('-');
        	console.log(mydate);
        	var day = parseInt(mydate[2]);
        	var month = parseInt(mydate[1]-1);
        	var year = parseInt(mydate[0]);
        	var dateArray = [year, month, day]

        	return dateArray;
        }
        console.log(c);
        console.log(d);

        var scd = sed(c);
        var pcd = sed(d);
        console.log(scd);
        console.log(pcd);
        // var date = new Date(scd)



//         var data = new google.visualization.DataTable(
//    {
//      cols: [{id: 'p', label: 'Parameter', type: 'string'},
//             {id: 'bud', label: 'Budgeted', type: 'number'},
//             {id: 'est', label: 'Estimated Completion Date', type: 'number'}],
//      rows: [{c:[{v: 'Schedule'}, {v: new Date(scd[0], scd[1], scd[2])},{v: new Date(pcd[0], pcd[1], pcd[2])}]} ]
//    }
// );
    var data = google.visualization.arrayToDataTable([
        ['Parameter', 'Budget', 'Estimate'],
        ['Schedule', new Date(scd[0], scd[1], scd[2]), new Date(pcd[0], pcd[1], pcd[2])]
        ]);

      var options = {
        // title: 'Project\'s Scheduled Performance',
        hAxis: {
        	scaleType: 'date'
        },
        legend: { position: 'top', alignment: 'end' },
        // colors: ['#e0440e', '#e6693e', '#ec8f6e', '#f3b49f', '#f6c7b6'],
        is3D: true
      };

      var chart = new google.visualization.BarChart(document.getElementById('shed'));


      chart.draw(data, options);
       $(window).resize(function(){
	   chart.draw(data, options);
	});
       
    }
     

    
}]);

app.controller('ManhoursController', ['$scope', '$http', function($scope, $http) {
	b = 1;
	p = 1;
	
    $http.get("/cpdashboard/inits/" + initiative.id + "/?format=json")
    .success(function(data) {
    	myData(data);
        // console.log(b);
    });
    
    function myData(data){

    	//a = data.scheduled_start_date;
    	am = data.actual_manhours;
    	bm = data.budgeted_manhours;
    	pm = data.projected_manhours;
        $scope.initiative = data;
        
        $scope.statuscode = data.status;
        $scope.statustext = data.statusText; 


        var data = new google.visualization.DataTable(
   {
     cols: [{id: 'p', label: 'Parameter', type: 'string'},
            {id: 'bud', label: 'Budget', type: 'number'},
            {id: 'est', label: 'Estimate', type: 'number'},
            {id: 'est', label: 'Actual', type: 'number'}],
     rows: [{c:[{v: 'Manhours'}, {v: bm},{v: pm},{v:am}]} ]
   }
)
    // var data = google.visualization.arrayToDataTable([
    //     ['Parameter', 'Budget', 'Estimate'],
    //     ['Cost', {v:bc}, {v:40000}], ]);

      var options = {
        // title: 'Project\'s Manhours Performance',
        legend: { position: 'top', alignment: 'end' },
        // colors: ['#e0440e', '#e6693e', '#ec8f6e', '#f3b49f', '#f6c7b6'],
        is3D: true
      };
      var chart = new google.visualization.BarChart(document.getElementById('man'));


      chart.draw(data, options);
       $(window).resize(function(){
	   chart.draw(data, options);
	});
       
    }
     

    
}]);



  app.controller('MyCtrl1', ['$scope', '$http',
    function($scope, $http) {

    	
    	$http.get("/cpdashboard/inits/?format=json")
    	.success(function(data){
    		$scope.initiatives = data;
    	});



       var data = google.visualization.arrayToDataTable([
        ['Parameter', 'Budget', 'Estimate'],
        ['Cost', parseFloat($scope.initiative.budgeted_cost), parseFloat($scope.initiative.projected_end_cost)],
        
        
      ]);
      var options = {
        title: 'Project\'s Cost Performance'
      };
      var chart = new google.visualization.BarChart(document.getElementById('chartdiv'));


      chart.draw(data, options);

	//   $(window).resize(function(){
	//    chart.draw(data, options);
	// });
    }

   
  ])
    .controller('MyCtrl2', ['$scope',
    function($scope) {
      var data = google.visualization.arrayToDataTable([
        ['Parameter', 'Budget', 'Estimate'],
        ['Scheduled', new Date(2016, 8, 9), new Date(2016, 11, 12)],
        
        
      ]);
      var options = {
        title: 'Project\'s Schedule Performance'
      };
      var chart = new google.visualization.BarChart(document.getElementById('date'));


      chart.draw(data, options);
      $(window).resize(function(){
	   chart.draw(data, options);
	});

//       $(window).resize(function(){
//    yourCartdrawChartfuntion();
// });
    }
  ]).controller('MyCtrl3', ['$scope',
    function($scope) {
      var data = google.visualization.arrayToDataTable([
        ['Parameter', 'Budget', 'Estimate'],
        ['Manhours', 100, 87],
        
        
      ]);
      var options = {
        title: 'Project\'s Manhours Performance'
      };
      var chart = new google.visualization.BarChart(document.getElementById('man'));


      chart.draw(data, options);
 //      $(window).resize(function(){
	//    chart.draw(data, options);
	// });


//       $(window).resize(function(){
//    yourCartdrawChartfuntion();
// });
    }
  ]).controller('InitiativeDetail', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
    	$http.get('/cpdashboard/inits/' + $routeParams.initiativeId + '/?format=json').success(function(data){
    		$scope.initiative = data;
    	});
 
    }
  ]);