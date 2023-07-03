function draw(){
  canvas = document.getElementById("main");
  if (!canvas.getContext) return -1;
  ctx = canvas.getContext("2d");
  ctx.fillStyle = "rgb(255, 255, 255)";
  var points1 = [
    [10,10],
    [90,10],
    [10,90],
    [90,90]];
  drawlines(ctx, points1, true);
}
function drawlines(ctx, points, fill=false){
  ctx.beginPath();
  ctx.moveTo(points[0][0],points[0][1]);
  for(var i=1; i<points.length; i++) ctx.lineTo(points[i][0],points[i][1]);
  if (fill) ctx.closePath();
  ctx.stroke();
}