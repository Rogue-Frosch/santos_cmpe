public class MyfirstJavaCode {
  public static void main(String[] args) {
    System.out.println("BS ECE 1-4 demo");
    for (int x = 10; x > -1; x--) {
      System.out.println(x);
 
      try {
        Thread.sleep(1000);
      } catch (InterruptedException ex) {}
    }
  }
}