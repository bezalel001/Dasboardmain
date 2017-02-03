var app = angular.module('cpdApp',['ngRoute']);

// 'use strict';

// /* Controllers */
// google.load('visualization', '1', {
//   packages: ['corechart']
// });

// google.setOnLoadCallback(function() {
//   angular.bootstrap(document.body, ['cpdApp']);
// });


app.controller('InitiativeController', ['$scope', '$routeParams', '$http', function($scope, $routeParams, $http) {
	$scope.name ='Michael Ogu';
	$scope.initiativeId = $routeParams.id;

app.config(['$routeProvider', 
	function($routeProvider){
		$routeProvider.
			when('/initiatives/dashboard/:id', {
				templateUrl: "/static/cpdashboard/app/partials/initiative-detail.html",
				controller: 'InitiativeController'
			}).
			otherwise({redirectTo: '/initiatives/dashboard/:id'});
			console.log('Me')
	}
	]);
 //$locationProvider.html5Mode(true);

 
  	

// 	b = 1;
// 	p = 1;
	
//     $http.get("/cpdashboard/inits/" + $routeParams.id + "/?format=json")
//     .success(function(data) {
//     	myData(data);
//         // console.log(b);
//     });
    
//     function myData(data){

//     	b = data.budgeted_cost;
//     	p = data.projected_end_cost;
//         $scope.initiative = data;
//         $scope.budget = data.budgeted_cost;
//         $scope.statuscode = data.status;
//         $scope.statustext = data.statusText; 


//         var data = new google.visualization.DataTable(
//    {
//      cols: [{id: 'p', label: 'Parameter', type: 'string'},
//             {id: 'bud', label: 'Budgeted Cost', type: 'number'},
//             {id: 'est', label: 'Estimated Cost at Completion', type: 'number'}],
//      rows: [{c:[{v: 'Cost'}, {v: b},{v: p}]}, ]
//    }
// )
//     // var data = google.visualization.arrayToDataTable([
//     //     ['Parameter', 'Budget', 'Estimate'],
//     //     ['Cost', {v:bc}, {v:40000}], ]);

//       var options = {
//         // title: 'Project\'s Cost Performance',
//         legend: { position: 'top', alignment: 'end' }
//       };
//       var chart = new google.visualization.BarChart(document.getElementById('mycost'));


//       chart.draw(data, options);
//        $(window).resize(function(){
// 	   chart.draw(data, options);
// 	});
       
//     }
     

    
}]);





