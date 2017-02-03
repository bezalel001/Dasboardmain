var app = angular.module('cpdApp', []);
app.controller('GraphController', ['$scope', 
    function($scope){
        $scope.myData = '40,60,55,72';
        $scope.name = "Michael";
    }]);

app.directive('bars', function($parse) {
  return {
    restrict: 'E',
    replace: true,
    template: '<div id="chart"></div>',
    link: function(scope, element, attrs) {
      var data = attrs.data.split(','),
        chart = d3.select('#chart')
        .append("div").attr("class", "chart")
        .selectAll('div')
        .data(data).enter()
        .append("div")
        .transition().ease("elastic")
        .style("width", function(d) {
          return d + "%";
        })
        .text(function(d) {
          var arr = ['Budgeted Cost', 'Projected Completion Cost', 'Scheduled Completion Date', 'Projected Completion Date'];
          return arr[Math.floor((Math.random() * 4) )];
        });
    }
  };
});

