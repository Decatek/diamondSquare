package dsquare.geom;

import massive.munit.util.Timer;
import massive.munit.Assert;
import massive.munit.async.AsyncFactory;


class VertexTest 
{
	var vert:Vertex;
	
	public function new() 
	{
		
	}
	
	@BeforeClass
	public function beforeClass():Void
	{
	}
	
	@AfterClass
	public function afterClass():Void
	{
	}
	
	@Before
	public function setup():Void
	{
	}
	
	@After
	public function tearDown():Void
	{
		vert = null;
	}
	
	@Test
	public function shouldCreateVertexAtZero():Void
	{
		vert = new Vertex();
		Assert.areEqual(vert.x, 0);
		Assert.areEqual(vert.y, 0);
		Assert.areEqual(vert.z, 0);
	}

	@Test
	public function shouldCreateVertexAtArbitraryPosition():Void
	{
		vert = new Vertex(10, 20, 30);
		Assert.areEqual(vert.x, 10);
		Assert.areEqual(vert.y, 20);
		Assert.areEqual(vert.z, 30);
	}

	@Test
	public function shouldGetMid():Void
	{
		var v1 = new Vertex(0, 0);
		var v2 = new Vertex(1, 1);
		var mid = Vertex.getMid(v1, v2);
		Assert.areEqual(mid.x, 0.5);
		Assert.areEqual(mid.y, 0.5);
	}
}
