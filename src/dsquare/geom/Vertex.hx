package dsquare.geom;

class Vertex {
	public var x:Float;
	public var y:Float;
	public var z:Float;

	public function new (x:Float = 0, y:Float = 0, z:Float = 0) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	/**
	 * Gets the midpoint of two vertices
	 * 
	 * @returns: Vertex the vertex at the mid point
	**/
	public static function getMid(a:Vertex, b:Vertex):Vertex {
		var mid:Vertex;
		var x = (a.x + b.x) / 2;
		var y = (a.y + b.y) / 2;
		return new Vertex(x, y);
	}
}
