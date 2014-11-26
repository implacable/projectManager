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

    function AddCommentService($http) {
        me = this;

        me.add_comment = function(content){
                $http.post('/user/add_comment/', {content: content})
                 .success(function(data) {
                    // Update old list of comments
                })
                .error(function(data) {
                    console.log(data);
                });
            }

        };

        me.get_comments = function(content){
               $http.post('/user/get_comments/', {content: content})
                 .success(function(data) {
                    // Update list of comments
                })
                .error(function(data) {
                    console.log(data);
                });
            }
        }

        return me;
    }

	angular
	    .module('Ticket');
		.service('ChangeTicketStatus', ChangeTicketStatus);
        .service('AddCommentService', AddCommentService);
})();