import org.openqa.selenium.By;
import org.openqa.selenium.By.ByTagName;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import org.junit.Assert;
import static org.junit.Assert.*;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.junit.Before;
import org.junit.Test;


public class websiteTest {
	

	   /** Fixture initialization (common initialization
	    *  for all tests). **/
		WebDriver driver;
	   @Before
	   public void setUp() {
		   System.setProperty("webdriver.chrome.driver","/home/omarj/Desktop/chromedriver");
			// Create a new instance of the Chrome driver
			driver = new ChromeDriver();
			
	        //Launch the Website
			driver.get("http://127.0.0.1:8000/");
			driver.findElement(By.cssSelector("input[name='username']")).sendKeys("ojawaad");
			driver.findElement(By.cssSelector("input[name='password']")).sendKeys("password123");
			driver.findElement(By.cssSelector("button[type='submit']")).click();			

	   }
	   
	   @Test public void update_test(){
//		   
		   List<WebElement> a=driver.findElements(By.className("clickable-row"));
		   a.get(1).click();
		   driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
		   driver.findElement(By.cssSelector("textarea[id='update_text']")).sendKeys("this is a test update");
		   driver.findElement(By.cssSelector("button[id='update_btn']")).click();
//		   Assert.assertNotNull(test);
		   }
	   
	   @Test public void ticket_test(){
		   driver.findElement(By.cssSelector("button[id='newTicketBtn']")).click();
		   driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
		   driver.findElement(By.cssSelector("input[name='location']")).sendKeys("testing");
		   driver.findElement(By.cssSelector("input[name='requestor']")).sendKeys("me");
		   driver.findElement(By.cssSelector("input[name='recipient']")).sendKeys("you");
		   driver.findElement(By.cssSelector("select[name='urgency']")).click();
		   driver.findElement(By.cssSelector("option[value='1']")).click();
		   driver.findElement(By.cssSelector("textarea[id='description']")).sendKeys("this is a test description");
		   driver.findElement(By.cssSelector("button[type='submit']")).click();
		   
 
		   driver.quit();
//		   Assert.assertNotNull(test);
		   }
	   
	   @Test public void ticket_test2(){
		   driver.findElement(By.cssSelector("button[id='newTicketBtn']")).click();
		   driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
		   driver.findElement(By.cssSelector("input[name='location']")).sendKeys("");
		   driver.findElement(By.cssSelector("input[name='requestor']")).sendKeys("");
		   driver.findElement(By.cssSelector("input[name='recipient']")).sendKeys("");
		   driver.findElement(By.cssSelector("select[name='urgency']")).click();
		   driver.findElement(By.cssSelector("option[value='2']")).click();
		   driver.findElement(By.cssSelector("textarea[id='description']")).sendKeys("this is a test description");
		   driver.findElement(By.cssSelector("button[type='submit']")).click();
		   

		   driver.quit();
//		   Assert.assertNotNull(test);
		   }
	   
	   
	   
	  
	
	
}