var app = app || {}

app.Poll = Backbone.Model.Extend({
	default: {
		title : '' ,
		votes :     ,
		user  : ''  ,
	},

	Upvote : function(){
		this.votes += 1;
	},
	DownVote :  function(){
		this.votes -= 1;
	}

})