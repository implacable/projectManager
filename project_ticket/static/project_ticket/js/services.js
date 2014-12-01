(function(){
    function ChangeTicketStatus($http) {
        me = this;

        // Reference this for example
        // _me.add_post = function(content, all_wall_post) {
        //     var url = location.pathname;
        //     var path = url.split('/');
        //     if (content !== ''){
	       //      $http.post('/user/add_wall_post/', {content: content, id: path[2]})
	       //   		.success(function(data) {
	       //              all_wall_post.unshift(data);
	       //          })
	       //          .error(function(data) {
	       //              console.log(data);
	       //          });
        //     }
        // };

        return me;
    }


	angular
	    .module('Ticket');
		.service('ChangeTicketStatus', ChangeTicketStatus);
})();