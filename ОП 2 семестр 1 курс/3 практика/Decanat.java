public class Decanat {

    private int room;
    private String nameFaculty;
    private String corps;
    private String telephone;
    private String nameDean;

    void setRoom(int room){

        this.room=room;
    }

    void  setCorps(String corps){

        this.corps=corps;
    }

    void setTelephone (String telephone){

        this.telephone=telephone;
    }

    void setNameDean (String nameDean){
        this.nameDean=nameDean;
    }

    Decanat(String nameFaculty){

        this.nameFaculty = nameFaculty;
    }

    public String toString(){
      return "Свойства деканата:\n" + "Факультет - " + this.nameFaculty + "\nНомер кабинета - "+ this.room +
              "\nКорпус - " + this.corps + "\nКонтактный телефон: " + this.telephone + "\nФамилия декана - " + this.nameDean;
    }
}

