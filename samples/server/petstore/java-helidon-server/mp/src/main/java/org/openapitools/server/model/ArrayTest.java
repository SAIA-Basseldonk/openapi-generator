/*
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.openapitools.server.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapitools.server.model.ReadOnlyFirst;
import jakarta.validation.constraints.*;
import jakarta.validation.Valid;


import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonValue;


public class ArrayTest  {
  
  private List<String> arrayOfString = null;

public enum ArrayWithUniqueItemsEnum {

    _1(String.valueOf("unique_item_1")), _2(String.valueOf("unique_item_2")), _3(String.valueOf("unique_item_3"));


    private String value;

    ArrayWithUniqueItemsEnum (String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    @Override
    @JsonValue
    public String toString() {
        return String.valueOf(value);
    }

    /**
     * Convert a String into String, as specified in the
     * <a href="https://download.oracle.com/otndocs/jcp/jaxrs-2_0-fr-eval-spec/index.html">See JAX RS 2.0 Specification, section 3.2, p. 12</a>
     */
	public static ArrayWithUniqueItemsEnum fromString(String s) {
        for (ArrayWithUniqueItemsEnum b : ArrayWithUniqueItemsEnum.values()) {
            // using Objects.toString() to be safe if value type non-object type
            // because types like 'int' etc. will be auto-boxed
            if (java.util.Objects.toString(b.value).equals(s)) {
                return b;
            }
        }
        throw new IllegalArgumentException("Unexpected string value '" + s + "'");
	}
	
    @JsonCreator
    public static ArrayWithUniqueItemsEnum fromValue(String value) {
        for (ArrayWithUniqueItemsEnum b : ArrayWithUniqueItemsEnum.values()) {
            if (b.value.equals(value)) {
                return b;
            }
        }
        throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
}

  private Set<ArrayWithUniqueItemsEnum> arrayWithUniqueItems = null;

  private List<List<Long>> arrayArrayOfInteger = null;

  private List<List<ReadOnlyFirst>> arrayArrayOfModel = null;

 /**
   * Get arrayOfString
   * @return arrayOfString
  **/
 @Size(min=0,max=3)  public List<String> getArrayOfString() {
    return arrayOfString;
  }

  /**
    * Set arrayOfString
  **/
  public void setArrayOfString(List<String> arrayOfString) {
    this.arrayOfString = arrayOfString;
  }

  public ArrayTest arrayOfString(List<String> arrayOfString) {
    this.arrayOfString = arrayOfString;
    return this;
  }

  public ArrayTest addArrayOfStringItem(String arrayOfStringItem) {
    this.arrayOfString.add(arrayOfStringItem);
    return this;
  }

 /**
   * Get arrayWithUniqueItems
   * @return arrayWithUniqueItems
  **/
  public Set<ArrayWithUniqueItemsEnum> getArrayWithUniqueItems() {
    return arrayWithUniqueItems;
  }

  /**
    * Set arrayWithUniqueItems
  **/
    @JsonDeserialize(as = LinkedHashSet.class)
  public void setArrayWithUniqueItems(Set<ArrayWithUniqueItemsEnum> arrayWithUniqueItems) {
    this.arrayWithUniqueItems = arrayWithUniqueItems;
  }

  public ArrayTest arrayWithUniqueItems(Set<ArrayWithUniqueItemsEnum> arrayWithUniqueItems) {
    this.arrayWithUniqueItems = arrayWithUniqueItems;
    return this;
  }

  public ArrayTest addArrayWithUniqueItemsItem(ArrayWithUniqueItemsEnum arrayWithUniqueItemsItem) {
    this.arrayWithUniqueItems.add(arrayWithUniqueItemsItem);
    return this;
  }

 /**
   * Get arrayArrayOfInteger
   * @return arrayArrayOfInteger
  **/
  public List<List<Long>> getArrayArrayOfInteger() {
    return arrayArrayOfInteger;
  }

  /**
    * Set arrayArrayOfInteger
  **/
  public void setArrayArrayOfInteger(List<List<Long>> arrayArrayOfInteger) {
    this.arrayArrayOfInteger = arrayArrayOfInteger;
  }

  public ArrayTest arrayArrayOfInteger(List<List<Long>> arrayArrayOfInteger) {
    this.arrayArrayOfInteger = arrayArrayOfInteger;
    return this;
  }

  public ArrayTest addArrayArrayOfIntegerItem(List<Long> arrayArrayOfIntegerItem) {
    this.arrayArrayOfInteger.add(arrayArrayOfIntegerItem);
    return this;
  }

 /**
   * Get arrayArrayOfModel
   * @return arrayArrayOfModel
  **/
  public List<List<ReadOnlyFirst>> getArrayArrayOfModel() {
    return arrayArrayOfModel;
  }

  /**
    * Set arrayArrayOfModel
  **/
  public void setArrayArrayOfModel(List<List<ReadOnlyFirst>> arrayArrayOfModel) {
    this.arrayArrayOfModel = arrayArrayOfModel;
  }

  public ArrayTest arrayArrayOfModel(List<List<ReadOnlyFirst>> arrayArrayOfModel) {
    this.arrayArrayOfModel = arrayArrayOfModel;
    return this;
  }

  public ArrayTest addArrayArrayOfModelItem(List<ReadOnlyFirst> arrayArrayOfModelItem) {
    this.arrayArrayOfModel.add(arrayArrayOfModelItem);
    return this;
  }


  /**
    * Create a string representation of this pojo.
  **/
  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ArrayTest {\n");
    
    sb.append("    arrayOfString: ").append(toIndentedString(arrayOfString)).append("\n");
    sb.append("    arrayWithUniqueItems: ").append(toIndentedString(arrayWithUniqueItems)).append("\n");
    sb.append("    arrayArrayOfInteger: ").append(toIndentedString(arrayArrayOfInteger)).append("\n");
    sb.append("    arrayArrayOfModel: ").append(toIndentedString(arrayArrayOfModel)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private static String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

