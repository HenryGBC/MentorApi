-- upgrade --
ALTER TABLE "mentor" DROP COLUMN "value";
-- downgrade --
ALTER TABLE "mentor" ADD "value" VARCHAR(120) NOT NULL;
