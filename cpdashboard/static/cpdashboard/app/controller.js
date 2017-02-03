var app = angular.module('cpdApp', ['ngRoute']);

'use strict';

/* Controllers */
google.load('visualization', '1', {
    packages: ['corechart', ]
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
	
    $http.get("/inits/" + initiative.id + "/?format=json")
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
	
    $http.get("/inits/" + initiative.id + "/?format=json")
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


       //#############################################################

       // schStartDate = sed(data.scheduled_start_date);
       // schEndDate = sed(data.scheduled_end_date);
       // actStartDate = sed(data.actual_start_date);
       // proEndDate = sed(data.projected_end_date);
       
       
       //var container = document.getElementById('shed');
       //var chart = new google.visualization.Timeline(container);
       //var dataTable = new google.visualization.DataTable();

       //dataTable.addColumn({ type: 'string', id: 'President' });
       //dataTable.addColumn({ type: 'date', id: 'Start' });
       //dataTable.addColumn({ type: 'date', id: 'End' });
       //dataTable.addRows([
       //  ['Budget', new Date(schStartDate[0], schStartDate[1], schStartDate[2]), new Date(schEndDate[0], schEndDate[1], schEndDate[2])],
       //  ['Estimate', new Date(actStartDate[0], actStartDate[1], actStartDate[2]), new Date(proEndDate[0], proEndDate[1], proEndDate[2])],
       //  ]);

       //chart.draw(dataTable);
       
    }
     

    
}]);

app.controller('ManhoursController', ['$scope', '$http', function($scope, $http) {
	b = 1;
	p = 1;
	
    $http.get("/inits/" + initiative.id + "/?format=json")
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


//**********************************************************************************************************
  app.controller('CompanyController', ['$scope', '$http', function ($scope, $http) {
      b = 1;
      p = 1;

      $http.get("/inits/" + initiative.id + "/?format=json")
      .success(function (data) {
          myData(data);
          // console.log(b);
      });

      function myData(data) {

          b = data.budgeted_cost;
          p = data.projected_end_cost;
          ac = data.actual_cost;
          console.log(ac);
          $scope.initiative = data;
          $scope.budget = data.budgeted_cost;
          $scope.statuscode = data.status;
          $scope.statustext = data.statusText;
          $scope.you = 'Zinariya';


          var data = google.visualization.arrayToDataTable([
           ['Task', 'Hours per Day'],
           ['Work', 33],
           ['Eat', 33],
           ['Commute', 33],
          ]);
          

          var options = {
              title: 'Company Controller',
              pieHole: 0.5,
              colors: ['#DC3912', '#FF9900', '#109618']
          };

          var chart = new google.visualization.PieChart(document.getElementById('company'));

          chart.draw(data, options);
          



          chart.draw(data, options);
          $(window).resize(function () {
              chart.draw(data, options);
          });

      }



  }]);

//***********************************************************************************
  app.controller('PieController1', ['$scope', '$http', function ($scope, $http) {
      b = 1;
      p = 1;

      $http.get("/inits/" + initiative.id + "/?format=json")
      .success(function (data) {
          myData(data);
          // console.log(b);
      });

      function myData(data) {

          b = data.budgeted_cost;
          p = data.projected_end_cost;
          ac = data.actual_cost;
          console.log(ac);
          $scope.initiative = data;
          $scope.budget = data.budgeted_cost;
          $scope.statuscode = data.status;
          $scope.statustext = data.statusText;
          $scope.me = 'Michael';

          var data = google.visualization.arrayToDataTable([
           ['Task', 'Hours per Day'],
           ['Work', 33],
           ['Eat', 33],
           ['Commute', 33],
           
          ]);

          var options = {
              title: 'Pie Controller 1',
              pieHole: 0.4,
              colors: ['#DC3912', '#FF9900', '#109618']
          };

          var chart = new google.visualization.PieChart(document.getElementById('pie1'));

          chart.draw(data, options);




          $(window).resize(function () {
              chart.draw(data, options);
          });

      }



  }]);

  //******************************************************************************
  app.controller('ObjectiveController1', ['$scope', '$http', function ($scope, $http) {
      

      $http.get("/goals/?format=json")
      .success(function (data) {
          myData(data);
          // console.log(b);
      });

      function myData(data) {

          
          $scope.b = 10;
          a = 'Ogu';
         
          $scope.objectives = data;
          for (item in data) {
              console.log(item['id']);
              consolr.log(a);
          }
          


      }



  }]);


  app.controller('ObjectivesController', ['$scope', '$http', function ($scope, $http) {
      b = 1;
      p = 1;

      $http.get("/goals/?format=json")
      .success(function (data) {
          myData(data);
          $scope.objectives = data;
      }).error(function (data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          console.log(data);
      });

      function myData(data) {
          $scope.goals = data;
          $scope.goal = data[0];

          //***********************************************************************************
         
          //************************************************************************************

          var charts = {

              init: function () {
                  var self = this;
                  $.each(data, function (index, objective) {
                      console.log(index + ':' + objective.description);
                     
                      charts.draw(objective.red, objective.amber, objective.green, objective.id.toString());
                  })
              },
              draw: function (red, amber, green, id) {

                  var data = new google.visualization.DataTable(
                    {
                        cols: [{ id: 'c', label: 'Color', type: 'string' },
                               { id: 'st', label: 'Status', type: 'number' }],
                        rows: [{ c: [{ v: 'At risk' }, { v: red }] },
                               { c: [{ v: 'Under pressure' }, { v: amber }] },
                               { c: [{ v: 'Performing to plan' }, { v: green }] }
                        ]
                    }
                    );

                  var options = {
                      width: 180,
                      height: 100,
                      title: '',
                      pieHole: 0.4,
                      colors: ['#DC3912', '#FF9900', '#109618'],
                      legend: { position: 'none' },
                      chartArea: {
                          left: 1,
                          right: 1, // !!! works !!!
                          bottom: 1,  // !!! works !!!
                          top: 1,
                          width: "100%",
                          height: "100%"
                      }
                  };
                  
                  var chart = new google.visualization.PieChart(document.getElementById(id));

                  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                  function selectHandler() {
                      var selectedItem = chart.getSelection()[0];
                      if (selectedItem) {
                          var colour = data.getValue(selectedItem.row, 0);
                          alert('Initiatives are ' + colour);
                      }
                  }

                  google.visualization.events.addListener(chart, 'select', selectHandler);
                  //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                  chart.draw(data, options);
              }
          }
          //&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
          
          google.charts.setOnLoadCallback(charts.init);
      
          }
   



  }]);

  app.controller('myCtrl', function ($scope, $http) {
      $http.get("/goals/?format=json")
      .then(function (response) {
          $scope.myWelcome = response.data;
      });
  });

  app.controller('ObjectiveController', ['$scope', '$http', function ($scope, $http) {
    

      $http.get("/goal/" + objective.id +"/?format=json")
      .success(function (data) {
          myData(data);
          $scope.obj = data;
      }).error(function (data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          console.log(data);
      });

      function myData(data) {
          $scope.goal = data;
          $scope.a = objective.id;
           red = data.red;
          amber = data.amber;
          green = data.green;
          $scope.red = data.red;

          var data = new google.visualization.DataTable(
   {
       cols: [{ id: 'c', label: 'Color', type: 'string' },
              { id: 'st', label: 'Status', type: 'number' }],
       rows: [{ c: [{ v: '% of initiatives with red status' }, { v: red }] },
              { c: [{ v: '% of initiatives with amber status' }, { v: amber }] },
              { c: [{ v: '% of initiatives with green status' }, { v: green }] }
       ]
   }
);

          var options = {
              title: '',
              pieHole: 0.4,
              colors: ['#DC3912', '#FF9900', '#109618'],
              legend: { position: 'none' }
          };

          var chart = new google.visualization.PieChart(document.getElementById('donutchart'));

          chart.draw(data, options);
   

          $(window).resize(function () {
              chart.draw(data, options);
          });


      }




  }]);
//**********************************************************************
  app.controller('AllObjectivesController', ['$scope', '$http', function ($scope, $http) {


      $http.get("/goal/" + objective.id + "/?format=json")
      .success(function (data) {
          myData(data);
          $scope.obj = data;
      }).error(function (data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          console.log(data);
      });

      function myData(data) {
          $scope.goal = data;
          $scope.a = objective.id;
          red = data.red;
          amber = data.amber;
          green = data.green;
          $scope.red = data.red;

          var data = new google.visualization.DataTable(
   {
       cols: [{ id: 'c', label: 'Color', type: 'string' },
              { id: 'st', label: 'Status', type: 'number' }],
       rows: [{ c: [{ v: '% of initiatives with red status' }, { v: red }] },
              { c: [{ v: '% of initiatives with green status' }, { v: green }] },
              { c: [{ v: '% of initiatives with amber status' }, { v: amber }] }
       ]
   }
);

          var options = {
              title: '',
              pieHole: 0.4,
              colors: ['#DC3912', '#FF9900', '#109618']
          };

          var chart = new google.visualization.PieChart(document.getElementById('donutchart'));

          chart.draw(data, options);


          $(window).resize(function () {
              chart.draw(data, options);
          });


      }




  }]);