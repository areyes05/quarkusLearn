package com.linquest.learn;

import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.is;

@QuarkusTest
public class AmigoResourceTest {

    @Test
    public void testHelloEndpoint() {
        given()
          .when().get("/amigo")
          .then()
             .statusCode(200)
             .body(is("hola amigos"));

        given()
            .when().get("/amigos")
            .then()
                .statusCode(404);
    }

    @Test
    public void test404() {
        given()
            .when().get("/amigoskis")
            .then().statusCode(404);
    }

}