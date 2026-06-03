package com.prac.boot.entity;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="emp")
public class Emp {
    @Id
    private int eid;
    private String ename;
    private double sal;
    private String dept;
    // Getters Setters
    public int getEid() { return eid; }
    public void setEid(int eid) { this.eid = eid; }
    public String getEname() { return ename; }
    public void setEname(String ename) { this.ename = ename; }
    public double getSal() { return sal; }
    public void setSal(double sal) { this.sal = sal; }
    public String getDept() { return dept; }
    public void setDept(String dept) { this.dept = dept; }
}
