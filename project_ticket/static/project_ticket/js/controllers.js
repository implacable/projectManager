(function(){
	function TicketController(){
		var me = this;
        me.ticket_status = '';
        me.comment_data = '';
        

        me.change_status = function(){
            console.log('Test');
            console.log(me.ticket_status);
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

// Todo: Add comment and get comments look at older code