(function(){
	function TicketController($scope){
		var me = this;
        me.ticket_status = '';
        $scope.items = [
            { id: 1, name: 'Queued' },
            { id: 2, name: 'In Progress' },
            { id: 3, name: 'Testing' },
            { id: 4, name: 'Completed' },
        ];


        me.change_status = function(){
            me.ticket_status = me.ticket_status + "1"
            console.log("Test");
        };
	}

	angular
		.module('Ticket', [])
		.config(function($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');

            $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
            $httpProvider.defaults.headers.post['charset'] = 'UTF-8';
            $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        })
        .controller('TicketController', TicketController)
})();