public class Main {
    public static void main(String[] args) {

        Decanat decanat = new Decanat("КИСИП");
        decanat.setRoom(123);
        decanat.setCorps("Серый");
        decanat.setTelephone("8(900)555-35-35");
        decanat.setNameDean("Скрыпников");

       System.out.println(decanat.toString());
    }
}
