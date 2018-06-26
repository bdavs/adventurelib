function draw() {
    
    console.log(rooms);
    var canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        var x = 5;
        var y = 5;
        var height = 25;
        var width = 25;
        var padding = 5;
        ctx.fillStyle = 'rgb(0,0,0)';
//    ctx.fillRect(x, y, width,height);
    


        for(countx = 1; countx < 8; countx++){
            x = (width + padding)*countx;
    	    for(county = 1; county < 8; county++){
	            y = (height + padding)*county;
                if(rooms[countx-1][county-1] == 1){  //visited room
                    ctx.fillStyle = 'rgb(200,200,200)';
                    ctx.fillRect(x, y, width, height);
	            }
	            else if(rooms[countx-1][county-1] == 2){  //current room
                    ctx.fillStyle = 'rgb(0,0,255)';
                    ctx.fillRect(x, y, width, height);
	            }
	            else if(rooms[countx-1][county-1] == 3){  //seen room
                    ctx.fillStyle = 'rgb(255,255,0)';
                    ctx.fillRect(x, y, width, height);
                }
                else{                            //unseen or nonexistant room
                    ctx.fillStyle = 'rgb(0,0,0)';
                    //ctx.fillRect(x, y, width, height);
	            }
	        }
        }
//    x = 5;
    
//    ctx.fillStyle = 'rgb(255,0,0)';
//    ctx.fillRect(x, y, width,height);
//    ctx.fillRect(150, 25, 100, 100);
//    ctx.fillStyle = 'rgba(255,255,255,1)';
//    ctx.fillRect(25, 25, 50, 50);
//    ctx.clearRect(45, 45, 60, 60);
//    ctx.strokeRect(50, 50, 50, 50);
  }
}


