// ng-controller = 'personController'
// Problem 14

	function personController($scope) {
		$scope.fname = 'Arif',
		$scope.lname = 'Uz Zaman',
		$scope.fullname = function() {
			return $scope.fname + ' ' + $scope.lname;
		}
	}