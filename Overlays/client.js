function draw(rooms) {
    
    console.log(rooms);
    var canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        var x = 5;
        var y = 5;
        var height = 25;
        var width = 25;
        var padding = 5;
        ctx.fillStyle = 'rgb(0,0,0)';
//    ctx.fillRect(x, y, width,height);

        for(countx = 0; countx < 7; countx++){
            x = (width + padding)*(countx+1);
    	    for(county = 0; county < 7; county++){
	            y = (height + padding)*(county+1);
                if(rooms[countx][county] == 1){  //visited room
                    ctx.fillStyle = 'rgb(200,200,200)';
                    ctx.fillRect(x, y, width, height);
	            }
	            else if(rooms[countx][county] == 2){  //current room
                    ctx.fillStyle = 'rgb(0,0,255)';
                    ctx.fillRect(x, y, width, height);
	            }
	            else if(rooms[countx][county] == 3){  //seen room
                    ctx.fillStyle = 'rgb(255,255,0)';
                    ctx.fillRect(x, y, width, height);
                }
                else{                            //unseen or nonexistant room
                    ctx.fillStyle = 'rgb(0,0,0)';
                    //ctx.fillRect(x, y, width, height);
	            }
	        }
        }
    }
}

function clearMap(){
     var canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
    
}
