class Outer{
	public static void main(String args[]){
		Outer o = new Outer();
		Outer.Inner i = o.new Inner(); //since inner class is non static, so need to call via object of outer
		Outer.StaticInner si = new Outer.StaticInner();
		TestInterface tf = new TestInterface(){
			public void love(){
				System.out.println("This to the AnonymousInner class");
			}
		};
		tf.love();
		TestInterface tf2 = ()->{  //only applicable for functional interface
				System.out.println("This to the AnonymousInner class using lamba function");
		};
		tf2.love();
	}
	Outer(){
		System.out.println("This to the outer class");
	}
	class Inner{
		Inner(){
			System.out.println("This to the Inner class");
		}
	}
	static class StaticInner{
		StaticInner(){
			System.out.println("This to the StaticInner class");
		}
	}
}
interface TestInterface{
	void love();
}